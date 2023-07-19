import pygame
import random

class Spinner():
    def __init__(self, x, y, spinner_image, surface):
        self.original_image = spinner_image
        self.image = self.original_image
        self.surface = surface
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.rotation_speed = random.uniform(40, 90)
        self.total_degrees_spun = 0
        self.last_animated = pygame.time.get_ticks()
        self.spinning = False

    def update(self):
        if self.spinning:
            self.spin()

    def spin(self):
        now = pygame.time.get_ticks()

        start_time = now
        opening_speed = self.rotation_speed

        if now - self.last_animated > 10:
            self.last_animated = now
            self.image = pygame.transform.rotate(self.original_image, -self.total_degrees_spun)
            old_center = self.rect.center
            self.rect = self.image.get_rect(center=old_center)
            self.total_degrees_spun = (self.total_degrees_spun + self. rotation_speed) % 360
            self.rotation_speed = opening_speed * 0.5 ** (pygame.time.get_ticks()/100 - start_time/100)

            if self.rotation_speed <= 0.01:
                self.spinning = False
                self.rotation_speed = random.uniform(40, 90)
                self.outcome()

    def outcome(self):
        if self.total_degrees_spun < 30:
            print("Your tokens pump 10x. We're all going to make it!")
        if self.total_degrees_spun >= 30 and self.total_degrees_spun < 60:
            print("Gary Gensler has entered the chat. Your tokens dump 90%.")
        if self.total_degrees_spun >= 60 and self.total_degrees_spun < 90:
            print("It's just a bit of FUD. No one cares.")
        if self.total_degrees_spun >= 90 and self.total_degrees_spun < 120:
            print("Rugged. Everything to zero.")
        if self.total_degrees_spun >= 120 and self.total_degrees_spun < 150:
            print("That whitepaper was well written, you aped in, but it was a scam. Lose 10 tokens.")
        if self.total_degrees_spun >= 150 and self.total_degrees_spun < 180:
            print("Early adopter airdrop! 10 tokens.")
        if self.total_degrees_spun >= 180 and self.total_degrees_spun < 210:
            print("Your tokens pump 5x. That Lambo suddenly seems cheaper.")
        if self.total_degrees_spun >= 210 and self.total_degrees_spun < 240:
            print("Your tokens dump by 45%. At least they didn't halve in value!")
        if self.total_degrees_spun >= 240 and self.total_degrees_spun < 270:
            print("You were airdropped a useless governance token! Nothing happens!")
        if self.total_degrees_spun >= 270 and self.total_degrees_spun < 300:
            print("Rugged. Everything to zero.")
        if self.total_degrees_spun >= 300 and self.total_degrees_spun < 330:
            print(f"You've seen {random.randint(500, 1000)} ads in the metaverse. You've been rewarded with a token!")
        if self.total_degrees_spun >= 330:
            print("You were airdropped a pointless NFT! Nothing happens!")
