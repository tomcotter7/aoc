class Robot:
    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        vel_x: int,
        vel_y: int,
        board_w: int,
        board_h: int,
    ) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.board_w = board_w
        self.board_h = board_h

    def tick(self) -> None:
        self.pos_x = (self.pos_x + self.vel_x) % self.board_w
        self.pos_y = (self.pos_y + self.vel_y) % self.board_h

    def get_quadrant(self) -> int | None:
        mp_w = self.board_w // 2
        mp_h = self.board_h // 2

        if self.pos_x == mp_w or self.pos_y == mp_h:
            return None

        right_half = self.pos_x > mp_w
        bottom_half = self.pos_y > mp_h
        return right_half + 2 * bottom_half
