# Det har smugit sig in kommentarer i stället för kod på några ställen. 
# Skriv färdigt testfallen test_empty_list och test_number_list.

# Returnerar summan av alla tal i listan
def sum_list(list):
    return None

def test_empty_list():
    expected = 0
    actual = sum_list([])
    assert actual == expected
    
def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([6]) == 6
    assert sum_list([-1, 0, 1]) ==  0
    assert sum_list([10, 8, -18, 4]) == 4