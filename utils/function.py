def create_insert_sql(values):
    result = "("
    # result += ",".join([ str(values[i]) for i in values])
    first = True
    for i in values:
        if first:
            first = False
            if isinstance(values[i],str):
                result += "'" + str(values[i]) + "'"
            else:
                result += str(values[i])
        else:
            if isinstance(values[i],str):
                result += ",'" + str(values[i]) + "'"
            else:
                result += "," + str(values[i])
    result += ")"
    return result


def create_update_sql(values):
    result = ''
    first = True
    for i in values:
        if first:
            first = False
            result += str(i) + " = '%s'"%(values[i])
        else:
            result += "," + str(i) + " = '%s'"%(values[i])            
    return result