def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old_reqs_dict = dict()
    for line in old_reqs.strip().splitlines():
        pkg, ver = line.split("==")
        old_reqs_dict[pkg] = ver

    result = list()
    for line in new_reqs.strip().splitlines():
        pkg, ver = line.split("==")

        seps = len(ver.split("."))

        for i in range(seps):
            if int(ver.split(".")[i]) > int(old_reqs_dict[pkg].split(".")[i]):
                result.append(pkg)
                break
            elif int(ver.split(".")[i]) == int(old_reqs_dict[pkg].split(".")[i]):
                continue
            else:
                break

    return result
