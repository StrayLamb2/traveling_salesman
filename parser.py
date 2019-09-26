import re


class Parser:
    def __init__(self):
        self.Source = ''  # Source = Source
        self.Dest = ''  # Dest = Destination
        self.Road_val = {}  # Road_val = {Road:Value}
        self.Road_ends = {}  # Road_ends = {Road:[Node_names]}
        self.Node = {}  # Node = {Name:[Road]}
        self.Traffic_pre = {}  # Traffic_pre = {Day:Traffic}
        self.Traffic_act = {}  # Traffic_act = {Day:Traffic}

    def parse(self, input_file):
        mode = ''
        with open(input_file) as roadmap:
            roadmap.seek(0)
            self.Source = re.match('<Source>([^<]*)</Source>', roadmap.readline()).group(1)
            self.Dest = re.match('<Destination>([^<]*)</Destination>', roadmap.readline()).group(1)
            for line in roadmap:
                if line == '<Roads>\n':
                    mode = 'R'
                elif line == '<Predictions>\n':
                    mode = 'P'
                    day = 1
                elif line == '<ActualTrafficPerDay>\n':
                    mode = 'A'
                    day = 1
                else:
                    if mode == 'R' and line != '</Roads>\n':
                        temp = re.match('([^;]*);\s([^;]*);\s([^;]*);\s([^(\n)]*)', line)
                        self.Road_val.update({temp.group(1): temp.group(4)})
                        self.Road_ends.setdefault(temp.group(1), [temp.group(2), temp.group(3)])
                        self.Node.setdefault(temp.group(2), []).append(temp.group(1))
                        self.Node.setdefault(temp.group(3), []).append(temp.group(1))
                    if mode == 'P' and line != '</Predictions>\n':
                        if line == '<Day>\n':
                            day += 1
                            roadmap.readline()
                        elif line == '</Day>\n':
                            continue
                        else:
                            temp = re.match('([^;]*);\s(.*)', line)
                            self.Traffic_pre.setdefault(temp.group(1), {}).update({day: temp.group(2)})
                    if mode == 'A' and line != '</ActualTrafficPerDay>\n':
                        if line == '<Day>\n':
                            day += 1
                            roadmap.readline()
                        elif line == '</Day>\n':
                            continue
                        else:
                            temp = re.match('([^;]*);\s(.*)', line)
                            self.Traffic_act.setdefault(temp.group(1), {}).update({day: temp.group(2)})