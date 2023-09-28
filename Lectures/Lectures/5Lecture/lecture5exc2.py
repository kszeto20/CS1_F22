def frame_string(str):
    top = '*' * (len(str) + 6)
    bottom = '*' * (len(str) + 6)
    print(top)
    print('**', str, '**')
    print(bottom, end = '')
    
    
frame_string("Spanish Inquisition")
print("\n")
frame_string("Ni")