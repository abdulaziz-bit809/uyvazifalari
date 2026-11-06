#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""18. Uy Vazifalari"""
import json, os
from datetime import datetime, timedelta
class Chores:
    def __init__(self):
        self.file = "chores.json"
        self.data = json.load(open(self.file)) if os.path.exists(self.file) else {}
    def save(self):
        json.dump(self.data, open(self.file,"w"), ensure_ascii=False, indent=2)
    def add(self, name, days, person):
        self.data[name] = {"freq":days, "person":person, "last":None}; self.save(); print("✅")
    def done(self, name):
        if name in self.data: self.data[name]["last"] = datetime.now().strftime("%Y-%m-%d"); self.save(); print("✅")
    def due(self):
        today = datetime.now()
        res = []
        for n,i in self.data.items():
            if i["last"] is None: res.append(f"{n} ({i['person']})")
            else:
                last = datetime.strptime(i["last"], "%Y-%m-%d")
                if (today-last).days >= i["freq"]: res.append(f"{n} ({i['person']})")
        return res
def main():
    ch = Chores()
    while True:
        print("\n1.Qoshish 2.Bajarildi 3.Bugungi 4.Chiqish")
        c = input("> ")
        if c=="1": ch.add(input("Vazifa: "), int(input("Kun: ")), input("Kim: "))
        elif c=="2": ch.done(input("Vazifa: "))
        elif c=="3":
            for d in ch.due(): print("•", d)
        elif c=="4": break
if __name__ == "__main__": main()
