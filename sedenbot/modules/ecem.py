# Copyright (C) 2020 TeamDerUntergang.
#
# SedenUserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SedenUserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from random import choice

from sedenbot import KOMUT
from sedenecem.core import edit, sedenify, get_translation
# ================= CONSTANT =================
FLEX_STRINGS = [
    "Abijim ben flex",
    "Ne lazım abijim",
    "çko ayp",
    "Yarrrraaaaa",
    "Ab ayp",
    "Führer ab",
    "Slak Ube",
    "Napim",
    "Ab sen kırakermisin.",
    "Config Meykır ab.",
    "Sen configi atmak ben teşekkür etmek.",
    "Mars işi Gönül işi.",
    "😳😳",
    "🥺", ]
# ================= CONSTANT =================
"""Copyright (c) @Sedenogen | 2020"""


@sedenify(pattern='^.flex$')
def flexify(message):
    flex(message)


def flex(message):
    # Flex Ab
    edit(message, choice(FLEX_STRINGS))


KOMUT.update({"flex": get_translation("flexInfo")})
