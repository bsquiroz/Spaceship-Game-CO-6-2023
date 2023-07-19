class Bullet:
    def __init__(self, image, center):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.is_visible = True
        self.is_alive = True

    def update(self, obj):
        if self.rect.colliderect(obj.rect):
            obj.is_alive = False
            self.is_alive = False

    def draw(self, sreen):
        sreen.blit(self.image, self.rect)
