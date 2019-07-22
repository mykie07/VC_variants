# map_coloring.py
# From Classic Computer Science Problems in Python Chapter 3
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from csp import Constraint, CSP
from typing import Dict, List, Optional


class VC_EX_CON3(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1,place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either place is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        # check the color assigned to place1 is not the same as the
        # color assigned to place2
        #    return (assignment[self.place1] == "N-Graphic" | assignment[self.place1] != "A-Graphic") and \
        #          (assignment[self.place2] == "Server" | assignment[self.place2] == "Gaming")

        if assignment[self.place1] == "N-Graphic" or assignment[self.place1] == "A-Graphic":
            if assignment[self.place2] == "Server" or assignment[self.place2] == "Gaming":
                return True

        return False
#
class VC_EX_CON2(Constraint[str, str]):


    def __init__(self, place1: str, place2: str, place3: str, place4: str) -> None:
        super().__init__([place1, place2, place3, place4])
        self.place1: str = place1
        self.place2: str = place2
        self.place3: str = place3
        self.place4: str = place4

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either place is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment or self.place3 not in assignment or \
                self.place4 not in assignment:
            return True
        # check the color assigned to place1 is not the same as the
        # color assigned to place2
        #    return (assignment[self.place1] == "N-Graphic" | assignment[self.place1] != "A-Graphic") and \
        #           (assignment[self.place2] == "Server" | assignment[self.place2] == "Gaming")

        if (assignment[self.place3] == "8" or assignment[self.place2] == "16") and assignment[self.place4] == "A-CPU":
            if assignment[self.place2] == "Server":
                return True

        return False


if __name__ == "__main__":
    variables: List[str] = ["VC_CHR_GRAPHIC_CARD", "VC_CHR_TYPE", "VC_CHR_MAIN_MEMORY", "VC_CHR_CPU"]
    #variables: List[str] = ["VC_CHR_GRAPHIC_CARD", "VC_CHR_TYPE"]

    domains: Dict[str, List[str]] = {}

    domains[variables[0]] = ["N-Graphic", "A-Graphic"]
    domains[variables[1]] = ["Laptop", "Office", "Gaming", "Server"]
    domains[variables[2]] = ["2", "4", "8", "16"]
    domains[variables[3]] = ["A-CPU", "I-CPU"]

    # for variable in variables:
    #     domains[variable] = ["Laptop", "Office", "Gaming", "Server"]

    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(VC_EX_CON3("VC_CHR_GRAPHIC_CARD", "VC_CHR_TYPE"))
    csp.add_constraint(VC_EX_CON2("VC_CHR_GRAPHIC_CARD", "VC_CHR_TYPE", "VC_CHR_MAIN_MEMORY", "VC_CHR_CPU"))
    # csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"))
    # csp.add_constraint(MapColoringConstraint("South Australia", "Northern Territory"))
    # csp.add_constraint(MapColoringConstraint("Queensland", "Northern Territory"))
    # csp.add_constraint(MapColoringConstraint("Queensland", "South Australia"))
    # csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
    # csp.add_constraint(MapColoringConstraint("New South Wales", "South Australia"))
    # csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
    # csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))
    # csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)
