class student:
    def __init__(self,name,marks) -> None:
        self.name=name
        self.marks=marks
    def avg_score(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f"Hi {self.name} your avg score is ",sum/3)


s1=student("Ayush",[90,89,99])
s1.avg_score()

        