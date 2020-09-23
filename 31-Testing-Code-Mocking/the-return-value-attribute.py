from unittest.mock import Mock

mock = Mock(return_value = 24)

print(mock.return_value)
mock.return_value = 24
print(mock())

stuntman = Mock()
stuntman.jump_off_building.return_value = "Oh no, my leg!"
stuntman.light_on_fire.return_value = "It's burns!"

print(stuntman.jump_off_building())
print(stuntman.light_on_fire())

