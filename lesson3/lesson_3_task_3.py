from mailing import Mailing
from address import Address

to_address = Address("426035", "Ижевск", "Союзная", "5a", "20")
from_address = Address("4455", "Краснодар", "Квасная", "54", "5")

mailing = Mailing(to_address, from_address, 546, "gaga")

print(mailing)
