import pyray as pr
import tree
import coin

class Main():
    def __init__(self):
        pr.init_window(800, 450, "Coin Chase")
        pr.set_target_fps(60)

        # Initialize camera
        camera = pr.Camera3D()
        camera.position = pr.Vector3(0.0, 2.0, 4.0)
        camera.target = pr.Vector3(0.0, 2.0, 0.0)
        camera.up = pr.Vector3(0.0, 1.0, 0.0)
        camera.fovy = 60.0
        camera.projection = pr.CameraProjection.CAMERA_PERSPECTIVE

        # Lock the cursor within game
        pr.disable_cursor()

        # Read user_selected map size
        self.map_size = None
        with open("test.txt") as f:
            self.map_size = int(f.read())

        # Initialize trees
        trees_list = list()
        for i in range(pr.get_random_value(10, 30)):
            pos = self.get_pos()
            tree_obj = tree.Tree()
            tree_obj.set_position(pos)
            trees_list.append(tree_obj)

        # Initialize coin
        pos = self.get_pos()
        coin_obj = coin.Coin()
        coin_obj.set_position(pos)

        # Initialize score
        score = 0

        while not pr.window_should_close():

            # Compute movement internally for simple controls
            pr.update_camera(camera, pr.CameraMode.CAMERA_FIRST_PERSON)

            pr.begin_drawing()
            pr.clear_background(pr.SKYBLUE)
            pr.begin_mode_3d(camera)

            # Draw the ground
            if self.map_size == 1:
                pr.draw_plane(pr.Vector3(0.0, 0.0, 0.0), pr.Vector2(32.0, 32.0), pr.BEIGE)
            elif self.map_size == 2:
                pr.draw_plane(pr.Vector3(0.0, 0.0, 0.0), pr.Vector2(64.0, 64.0), pr.BEIGE)

            # Insert trees into the map
            for item in trees_list:
                pr.draw_cube(pr.Vector3(item.get_position_x(), 1, item.get_position_z()), 0.5, 2, 0.5, pr.BROWN)
                pr.draw_cube(pr.Vector3(item.get_position_x(), 3, item.get_position_z()), 3, 3, 3, pr.GREEN)

            # Draw coin
            pr.draw_cube(pr.Vector3(coin_obj.get_position_x(), 1.3, coin_obj.get_position_z()), 0.5, 0.5, 0.5, pr.GOLD)

            # Get camera position
            camera_pos = pr.Vector2(camera.position.x, camera.position.z)

            # Prevent player from leaving map
            if self.map_size == 1:
                if (pr.check_collision_point_line(camera_pos, pr.Vector2(16, 16), pr.Vector2(16, -16), 1)
                        or pr.check_collision_point_line(camera_pos, pr.Vector2(16, 16), pr.Vector2(-16, 16), 1)
                        or pr.check_collision_point_line(camera_pos, pr.Vector2(16, -16), pr.Vector2(-16, -16), 1)
                        or pr.check_collision_point_line(camera_pos, pr.Vector2(-16, -16), pr.Vector2(-16, 16), 1)):
                    camera.position = pr.Vector3(0.0, 2.0, 4.0)
            elif self.map_size == 2:
                if (pr.check_collision_point_line(camera_pos, pr.Vector2(32, 32), pr.Vector2(32, -32), 1)
                        or pr.check_collision_point_line(camera_pos, pr.Vector2(32, 32), pr.Vector2(-32, 32), 1)
                        or pr.check_collision_point_line(camera_pos, pr.Vector2(32, -32), pr.Vector2(-32, -32), 1)
                        or pr.check_collision_point_line(camera_pos, pr.Vector2(-32, -32), pr.Vector2(-32, 32), 1)):
                    camera.position = pr.Vector3(0.0, 2.0, 4.0)

            # Player collecting coin
            if (pr.check_collision_point_line(camera_pos, pr.Vector2(coin_obj.get_position_x() - 0.5,
                                                                     coin_obj.get_position_z() - 0.5),
                                              pr.Vector2(coin_obj.get_position_x() + 0.5, coin_obj.get_position_z() +
                                                                                          0.5),
                                              1)):
                score += 1
                pos = self.get_pos()
                coin_obj.set_position(pos)

            pr.end_mode_3d()

            # Timer and score
            pr.draw_text(str(round(pr.get_time() // 60)) + ":" + str(round(pr.get_time() % 60)), 10, 10, 30,
                         pr.RED)
            pr.draw_text(str(score), 775, 10, 30, pr.BLUE)

            # Game over
            if pr.get_time() >= 10:
                pr.gui_message_box(pr.Rectangle(pr.get_window_position().x // 2, pr.get_window_position().y // 2, 400,
                                                300), "Game Over", "Your score was: " + str(score),
                                   "Press 'Esc' to quit")

            pr.end_drawing()

    def get_pos(self):
        if self.map_size == 1:
            x_pos = pr.get_random_value(-14, 14)
            z_pos = pr.get_random_value(-14, 14)
        elif self.map_size == 2:
            x_pos = pr.get_random_value(-30, 30)
            z_pos = pr.get_random_value(-30, 30)

        pos = pr.Vector3(x_pos, 1, z_pos)
        return pos

    def close_window(self):
        pr.close_window()