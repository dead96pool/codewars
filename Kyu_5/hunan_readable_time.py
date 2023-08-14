

def make_readable(seconds):    
    """time_list = []
 
    for i in [3600, 60, 1]:
        val = int(seconds/i)
        time_list.append(str(val).zfill(2))
        seconds -= val*i

    return ":".join(time_list)
    """

    time = "{:02}:{:02}:{:02}".format(seconds // 3600, seconds // 60 % 60, seconds % 60)

    return time


def assert_equals(output, expected):
    #print(output == expected)
    pass
if __name__ == "__main__":
    #assert_equals(make_readable(0), "00:00:00")
    #assert_equals(make_readable(5), "00:00:05")
    #assert_equals(make_readable(60), "00:01:00")
    assert_equals(make_readable(86399), "23:59:59")
    #assert_equals(make_readable(359999), "99:59:59")
    assert_equals(make_readable(34073), "09:27:53")
    assert_equals(make_readable(51340), "14:15:40")
    assert_equals(make_readable(75282), "20:54:42")
    assert_equals(make_readable(21738), "06:02:18")
    assert_equals(make_readable(86347), "23:59:07")