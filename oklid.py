import math #modül çağırma


points = [(1, 2), (4, 6), (5, 8), (9, 12), (0, 3)]


def euclideanDistance(point1, point2): #Öklid mesafesi fonk. kullanılması
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)  #formül


distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


min_distance = min(distances)
print("Minimum mesafe:", min_distance)
