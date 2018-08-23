
def ftoc (f, _max, step):
    try:
        assert f <= _max
        c = ((f - 32) * 5) / 9
        print("%4.1d:%8.2f" % (f, c))
        ftoc(f+step, _max, step)
    except:
        return

ftoc(0, 100, 20)
