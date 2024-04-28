var = 1
def function():
    name = 'space'
    def function():
        global var
        name = 'cosmos'
        var += 23
        print('name:', name, ', var:', var)
    print('name:', name, ', var:', var)
    function()
function()