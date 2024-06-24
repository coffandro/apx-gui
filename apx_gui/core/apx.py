# apx.py
#
# Copyright 2023 Mirko Brombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import shlex
import json

from apx_gui.core.apx_entities import ApxEntityBase, Subsystem, Stack, PkgManager


class Apx(ApxEntityBase):
    def subsystems_list(self) -> list[Subsystem]:
        command = "subsystems list --json"
        status, output = self._run_apx_command(command)
        if not status:
            return []

        output = output[output.index("[") : output.rindex("]") + 1]
        subsystems_data = json.loads(output)
        subsystems: list[Subsystem] = []

        for data in subsystems_data:
            stack = Stack(
                data["Stack"]["Name"],
                data["Stack"]["Base"],
                data["Stack"]["Packages"],
                data["Stack"]["PkgManager"],
                data["Stack"]["BuiltIn"],
            )
            subsystem = Subsystem(
                data["InternalName"],
                data["Name"],
                stack,
                data["Status"],
                shlex.split(f"{self._get_apx_command()} {data['Name']} enter"),
                data["ExportedPrograms"],
            )
            subsystems.append(subsystem)

        return subsystems

    def stacks_list(self) -> list[Stack]:
        command = "stacks list --json"
        status, output = self._run_apx_command(command)
        if not status:
            return []

        output = output[output.index("[") : output.rindex("]") + 1]
        stacks_data = json.loads(output)
        stacks: list[Stack] = []

        for data in stacks_data:
            stack = Stack(
                data["Name"],
                data["Base"],
                data["Packages"],
                data["PkgManager"],
                data["BuiltIn"],
            )
            stacks.append(stack)

        return stacks

    def pkgmanagers_list(self) -> list[PkgManager]:
        command = "pkgmanagers list --json"
        status, output = self._run_apx_command(command)
        if not status:
            return []

        output = output[output.index("[") : output.rindex("]") + 1]
        pkgmanagers_data = json.loads(output)
        pkgmanagers: list[PkgManager] = []
        for data in pkgmanagers_data:
            pkgmanager = PkgManager(
                data["Name"],
                data["NeedSudo"],
                data["CmdAutoRemove"],
                data["CmdClean"],
                data["CmdInstall"],
                data["CmdList"],
                data["CmdPurge"],
                data["CmdRemove"],
                data["CmdSearch"],
                data["CmdShow"],
                data["CmdUpdate"],
                data["CmdUpgrade"],
                data["BuiltIn"],
            )
            pkgmanagers.append(pkgmanager)

        return pkgmanagers
