package main

import (
	"fmt"
	"log"
	"math/rand"
	"strings"
	"time"
	"os"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

type Player struct {
	Name string
	Role string
}

func main() {
	bot, err := tgbotapi.NewBotAPI(os.Getenv("BOT_TOKEN"))
	if err != nil {
		log.Panic(err)
	}

	bot.Debug = true

	log.Printf("Authorized on account %s", bot.Self.UserName)

	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates, err := bot.GetUpdatesChan(u)

	for update := range updates {
		if update.Message == nil { // ignore any non-Message Updates
			continue
		}

		pieces := strings.Split(update.Message.Text, "\n")

		var names []string
		response := "Без ролей:\n\n"
		for _, name := range pieces {
			pieces = pieces[1:]
			if name == "-" {
				break
			}

			names = append(names, name)
		}

		if len(names) < 3 {
			msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Маловато людей")

			bot.Send(msg)

			continue
		}

		rand.Seed(time.Now().UnixNano())
		rand.Shuffle(len(names), func(i, j int) { names[i], names[j] = names[j], names[i] })

		var badCount int
		if len(names) > 9 {
			badCount = 3
		} else if len(names) > 6 {
			badCount = 2
		} else {
			badCount = 1
		}

		var players []Player

		for i, name := range names {
			var role string
			if i < badCount {
				role = "Мафия"
			} else {
				role = "Мирный"
			}
			players = append(players, Player{name, role})
		}

		if badCount > 1 {
			players[0].Role = "Дон"
		}

		players[badCount].Role = "Комиссар"

		rand.Shuffle(len(players), func(i, j int) { players[i], players[j] = players[j], players[i] })

		for i, player := range players {
			response += fmt.Sprintf("%d. %s\n", i + 1, player.Name)
		}

		msg := tgbotapi.NewMessage(update.Message.Chat.ID, response)

		bot.Send(msg)

		response = "С ролями:\n\n"

		for i, player := range players {
			response += fmt.Sprintf("%d. %s - %s\n", i + 1, player.Name, player.Role)
		}

		msg = tgbotapi.NewMessage(update.Message.Chat.ID, response)

		bot.Send(msg)
	}
}
