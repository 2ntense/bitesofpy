def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
       its octal representation.

       In Unix you have user, group and other permissions,
       each can have read (r), write (w), and execute (x)
       permissions expressed by r, w and x.

       Each has a number:
       r = 4
       w = 2
       x = 1

       So this leads to the following input/ outputs examples:
       rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
       rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
       r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """
    if len(rwx) != 9:
        raise ValueError

    octal_repr = {
        "r": 4,
        "w": 2,
        "x": 1,
        "-": 0
    }

    permissions = [rwx[0:3], rwx[3:6], rwx[6:9]]

    result = []
    for perm in permissions:
        if perm[0] not in "-r" or perm[1] not in "-w" or perm[2] not in "-x":
            raise ValueError

        octal = 0
        for c in perm:
            octal += octal_repr [c]

        result.append(str(octal))

    return "".join(result)


print(get_octal_from_file_permission("rwxrwxrw-"))