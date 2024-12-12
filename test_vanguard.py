import unittest

import pygame
from RPG_Project_Vanguard import speed_normalization, colision_management, move

class TestStringMethods(unittest.TestCase):

    def test_speed_normalization(self):
        self.assertEqual(speed_normalization(movement_keys=[True, True, False, True], player_speed=200, delta_time=0.017), (200 * 0.017) / 1.41421)
        self.assertEqual(speed_normalization(movement_keys=[True, False, False, False], player_speed=200, delta_time=0.016), (200 * 0.016) / 1)
        self.assertEqual(speed_normalization(movement_keys=[False, False, False, False], player_speed=200, delta_time=0.017), (200 * 0.017) / 1)

    def test_colision_detection(self):
        self.assertEqual(colision_management(pygame.Rect(15, 5, 5, 5), 15, 5, 15, 5, [pygame.Rect(5, 5, 5, 5), pygame.Rect(5, 25, 5, 5), pygame.Rect(25, 5, 5, 20), pygame.Rect(25, 25, 5, 5)], {}), (15, 5, None))
        self.assertEqual(colision_management(pygame.Rect(200, 300, 5, 5), 210, 310, 200, 300, [pygame.Rect(5, 5, 5, 5), pygame.Rect(5, 25, 5, 5), pygame.Rect(25, 5, 5, 20), pygame.Rect(25, 25, 5, 5)], {}), (200, 300, None))
        self.assertEqual(colision_management(pygame.Rect(5, 5, 5, 5), 15, 5, 5, 5, [pygame.Rect(5, 5, 5, 5), pygame.Rect(5, 25, 5, 5), pygame.Rect(25, 5, 5, 20), pygame.Rect(25, 25, 5, 5)], {}), (15, 5, None)) 
        self.assertEqual(colision_management(pygame.Rect(14, 5, 5, 5), 15, 5 , 14, 5, [pygame.Rect(5, 5, 5, 5), pygame.Rect(5, 25, 5, 5), pygame.Rect(25, 5, 5, 20), pygame.Rect(25, 25, 5, 5)], {}), (14, 5, None))
        self.assertEqual(colision_management(pygame.Rect(19, 5, 5, 5), 15, 5 , 19, 5, [pygame.Rect(5, 5, 5, 5), pygame.Rect(5, 25, 5, 5), pygame.Rect(25, 5, 5, 20), pygame.Rect(25, 25, 5, 5)], {}), (19, 5, None))
        self.assertEqual(colision_management(pygame.Rect(21, 5, 5, 5), 15, 5 , 21, 5, [pygame.Rect(5, 5, 5, 5), pygame.Rect(5, 25, 5, 5), pygame.Rect(25, 5, 5, 20), pygame.Rect(25, 25, 5, 5)], {}), (15, 5, None))
        self.assertEqual(colision_management(pygame.Rect(21, 10, 5, 5), 15, 5 , 21, 10, [pygame.Rect(5, 5, 5, 5), pygame.Rect(5, 25, 5, 5), pygame.Rect(25, 5, 5, 20), pygame.Rect(25, 25, 5, 5)], {}), (15, 10, None))
        self.assertEqual(colision_management(pygame.Rect(21, 5, 5, 5), 15, 5, 21, 5, [pygame.Rect(5, 5, 5, 5), pygame.Rect(5, 25, 5, 5), pygame.Rect(25, 5, 5, 20), pygame.Rect(25, 25, 5, 5)], {}), (15, 5, None))

if __name__ == '__main__':
    unittest.main()