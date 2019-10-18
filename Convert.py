from math import sin, cos, radians, tan

c = float(input("Chord Length: ")) * 1000  # chord scale
AoT = radians(float(input("Angle of Twist: ")))  # input: degrees stored: radians
Section = input("Airfoil Section: ")
offset = float(input("Offset: ")) * 1000
x_wing = float(input("Y Value: ")) * 1000
dihedral = radians(5.0)  # radians

path = input("Relative Input Points File Path: ")
raw_data = open(path).readlines()
points = [[c*float(x) for x in point.split(',')] for point in raw_data]

for point in points:
    x, y = point
    point[0] = x*cos(AoT) + y*sin(AoT)
    point[1] = y*cos(AoT) - x*sin(AoT)

output = []
for point in points:
    x, y = point
    output.append(
        [
            x_wing,
            x - offset,
            y - x_wing*tan(dihedral)
        ]
    )

results = open(path + "_" + Section + "_processed.txt", 'w')
for x, y, z in output:
    out = str(x) + " " + str(y) + " " + str(z) + "\n"
    results.write(out)
results.flush()
results.close()
