import pygame
import random

class Spinner():

    def __init__(self, x, y, spinner_image, display, degrees, contestant):
        # set display and x, y coordinates
        self.display = display
        self.x = x
        self.y = y

        # load image
        self.original_image = spinner_image
        self.rect = self.original_image.get_rect(topleft=(self.x, self.y))
        # spin to previous position
        self.total_degrees_spun = degrees
        self.image = pygame.transform.rotate(self.original_image, -self.total_degrees_spun)
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)

        # load contestant
        self.contestant = contestant

        # set random rotation speed, check time and set spinning to false
        self.rotation_speed = random.uniform(40, 500)
        self.last_animated = pygame.time.get_ticks()
        self.spinning = False

        # initiate spinner outcome text and pass empty string
        self.font = pygame.font.Font('fonts/proxima_nova.ttf', 36)
        self.text = ''
        self.textimg = self.font.render(self.text, False, (0, 0, 0))
        self.textrect = self.textimg.get_rect(topleft=(self.x, self.y + 775))

    def update(self):
        if self.spinning:
            self.spin()

    def spin(self):
        # remove any text
        if self.text != '':
            self.text = ''
            self.textimg = self.font.render(self.text, False, (0, 0, 0))

        # establish time now
        now = pygame.time.get_ticks()

        # establish when spinning started and the opening roattion speed
        start_time = now
        opening_speed = self.rotation_speed

        # establish latency of updates
        if now - self.last_animated > 40:
            self.last_animated = now

            self.image = pygame.transform.rotate(self.original_image, -self.total_degrees_spun)
            old_center = self.rect.center
            self.rect = self.image.get_rect(center=old_center)
            self.total_degrees_spun = (self.total_degrees_spun + self. rotation_speed) % 360
            # reduce rotation speed through exponential decay
            self.rotation_speed = opening_speed * 0.5 ** (pygame.time.get_ticks()/100 - start_time/100)

            if self.rotation_speed <= 0.01:

                self.spinning = False
                self.rotation_speed = random.uniform(40, 500)
                self.outcome()

    def outcome(self):
        pumps = ["We're all going to make it!",
                 "That Lambo suddenly seems cheaper.",
                 "Time to start a youtube channel.",
                 "You could be a VC thought leader!",
                 "Definitely still not the top."]

        dumps = ["Gary Gensler has entered the chat.",
                 "A major exchange has collapsed.",
                 "Maximum pain.",
                 '"Steady lads, deploying more capital."']

        scams = ["That whitepaper was well written, you aped in, but it was a scam.",
                 "They're open about it being a ponzi, but it's still a ponzi.",
                 "Those 10,000 cartoon pictures were not the next big thing."]

        if self.total_degrees_spun < 30:
            self.text = f"Your tokens pump 10x. {pumps[random.randint(0, len(pumps) - 1)]}"
            self.contestant.score *= 10
        if self.total_degrees_spun >= 30 and self.total_degrees_spun < 60:
            self.text = f"{dumps[random.randint(0, len(dumps) - 1)]} Your tokens dump 90%."
            self.contestant.score = round(self.contestant.score * 0.1)
        if self.total_degrees_spun >= 60 and self.total_degrees_spun < 90:
            self.text = "It's just FUD. No one cares."
        if self.total_degrees_spun >= 90 and self.total_degrees_spun < 120:
            self.text = "Rugged. Everything to zero."
            self.contestant.score = 0
        if self.total_degrees_spun >= 120 and self.total_degrees_spun < 150:
            self.text =  f"{scams[random.randint(0, len(scams) - 1)]} Lose 10 tokens."
            self.contestant.score = max(0, self.contestant.score - 10)
        if self.total_degrees_spun >= 150 and self.total_degrees_spun < 180:
            self.text = "Early adopter airdrop! Receive 10 tokens."
            self.contestant.score += 10
        if self.total_degrees_spun >= 180 and self.total_degrees_spun < 210:
            self.text = f"Your tokens pump 5x. {pumps[random.randint(0, len(pumps) - 1)]}"
            self.contestant.score *= 5
        if self.total_degrees_spun >= 210 and self.total_degrees_spun < 240:
            self.text = "Your tokens dump by 45%. At least they didn't halve in value!"
            self.contestant.score = round(self.contestant.score * 0.55)
        if self.total_degrees_spun >= 240 and self.total_degrees_spun < 270:
            self.text = "You were airdropped a useless governance token! Nothing happens!"
        if self.total_degrees_spun >= 270 and self.total_degrees_spun < 300:
            self.text = "Rugged. The founder is living it up in the Bahamas."
            self.contestant.score = 0
        if self.total_degrees_spun >= 300 and self.total_degrees_spun < 330:
            self.text = f"You've seen {random.randint(500, 1000)} ads in the metaverse. You've been rewarded with a token!"
            self.contestant.score += 1
        if self.total_degrees_spun >= 330:
            self.text = "You were airdropped a pointless NFT! Nothing happens!"

        self.textimg = self.font.render(self.text, True, (0, 0, 0))
