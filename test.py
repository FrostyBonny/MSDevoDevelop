class Code:
    SUCCESS = 0
    NO_PARAM = 1
    ERROR =-1

    msg = {
        "0": "success",
        NO_PARAM: "param error",
        "-1":"error"
    }

def test(a = Code.SUCCESS,b = Code.msg[a]):
    print(a,b)

test()