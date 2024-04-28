list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def matrix():
    for i in list_:
        print(*i)
matrix()
print()
def new_matrix():
    list_[0][0:3] = list_[0][::-1]
    list_[1][0:3] = list_[1][::-1]
    list_[2][0:3] = list_[2][::-1]
    for i in list_:
        print(*i)
new_matrix()