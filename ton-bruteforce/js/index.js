import TonWeb from "tonweb";
import tonMnemonic from "tonweb-mnemonic";
import {setTimeout} from "timers/promises";

///////////////////////////////////////////////

const tonWeb = new TonWeb();
const mnemonic = tonMnemonic.wordlists.EN;

///////////////////////////////////////////////

const configuration = getConfiguration('prod')
console.log(configuration)
console.log('--------------------------------------------------')
const foundMnemonic = await findAnswer(configuration.knownMnemonic, configuration.knownAddress)
console.log('Found mnemonic:', foundMnemonic)
const keyPair = await tonMnemonic.mnemonicToKeyPair(foundMnemonic)
await sendTon(keyPair.secretKey, configuration.knownAddress, configuration.toAddress, configuration.amount, configuration.message)

///////////////////////////////////////////////

function getConfiguration(env = 'prod') {
    if (env === 'test') {
        return getTestConfiguration()
    }

    if (env === 'dev') {
        return getDevConfiguration()
    }

    return getProductionConfiguration()
}

function getProductionConfiguration() {
    return {
        knownMnemonic: [
            ['blast', 'burst'], 'crater',
            'virus', 'nation',
            'roof', 'notice',
            'nut', 'round',
            'stadium', 'december',
            'defy', 'execute',
            ['game', 'play'], 'wear',
            'helmet', 'today',
            'salmon', 'cool',
            'tuition', 'loud',
            'cattle', ['fresh', 'juice'],
            'act', '?',
        ],
        knownAddress: 'EQB-D2AH3qajK1bEExb7gIX0r-qeAMF6jUUf2uC9lA_x89zT',
        // https://ton.org/address/
        toAddress: 'UQAoByMcbBxImxO1ggeZWUejsqLJ9emt4lb-eBqOHxINgLQs',
        amount: '500',
        message: '',
    }
}

async function matchesAddress(mnemonic, address) {
    const keyPair = await tonMnemonic.mnemonicToKeyPair(mnemonic)
    const wallet = new tonWeb.wallet.all.v3R2(null, {publicKey: keyPair.publicKey})
    const addressObject = await wallet.getAddress();
    const addressFromMnemonic = addressObject.toString(true, true, true);

    return addressFromMnemonic === address
}

function showCombinationsAmount(optionsList) {
    let combinations = 1;
    optionsList.forEach(options => combinations *= options.length)
    console.log(`Combinations amount: ${combinations}`)
}

async function findAnswer(knownMnemonic, targetAddress) {
    let unknownIndexes = [];
    let unknownIndexesOptions = [];
    let currentState = [];
    knownMnemonic.forEach((item, index) => {
        if (Array.isArray(item)) {
            unknownIndexes.push(index)
            unknownIndexesOptions.push(item)
        } else if (item === '?') {
            unknownIndexes.push(index)
            unknownIndexesOptions.push(mnemonic)
        } else {
            currentState[index] = item
        }
    })

    showCombinationsAmount(unknownIndexesOptions)

    async function bruteforce(unknownIndexIndex) {
        if (unknownIndexIndex === 1) {
        }

        let unknownIndex = unknownIndexes[unknownIndexIndex]
        let options = unknownIndexesOptions[unknownIndexIndex]

        for (let i = 0; i < options.length; i++) {
            currentState[unknownIndex] = options[i]

            if (unknownIndexIndex + 1 < unknownIndexes.length) {
                if (await bruteforce(unknownIndexIndex + 1)) {
                    return true
                }
            } else {
                let isValid = await tonMnemonic.validateMnemonic(currentState)

                if (isValid && await matchesAddress(currentState, targetAddress)) {
                    return true
                }
            }
        }

        return false
    }

    const successful = await bruteforce(0)

    if (successful) {
        return currentState
    }

    throw new Error('Nothing found!')
}

async function waitSeconds(seconds = 1) {
    await setTimeout(seconds * 1000)
}

async function getSeqNo(wallet, sk) {
    let seqNo = await wallet.methods.seqno().call();

    if (seqNo) {
        return seqNo;
    }

    await waitSeconds()
    await wallet.deploy(sk).send()
    console.log('Deploy sent')

    let secondsToWait = 1
    while (seqNo === null) {
        console.log(`SeqNo is null, waiting ${secondsToWait}s`)
        await waitSeconds(secondsToWait)
        secondsToWait *= 2
        if (secondsToWait > 10) {
            secondsToWait = 10
        }

        seqNo = await wallet.methods.seqno().call()
    }

    return seqNo
}

async function sendTon(fromSK, fromAddress, to, amount, message = 'Test') {
    const wallet = new tonWeb.wallet.all.v3R2(new TonWeb.HttpProvider(), {address: fromAddress})

    const seqNo = await getSeqNo(wallet, fromSK)
    console.log(`SeqNo: ${seqNo}`)

    const transfer = wallet.methods.transfer({
        secretKey: fromSK,
        toAddress: to,
        amount: TonWeb.utils.toNano(amount),
        seqno: seqNo,
        payload: message,
        sendMode: 3,
    });

    await waitSeconds();

    const result = await transfer.send();
    console.log(`Send result:`);
    console.log(result);
}
