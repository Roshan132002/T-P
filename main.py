def outer():
    name="Roshan"

    def inner():
        nonlocal name
        print(name)
        name="Decode"
        
    inner()
    print(name)

outer()