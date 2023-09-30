python early hide:

    @renpy.atl_warper
    def rideby(t):
        # return t ** 2 * 0.98 + 0.02
        # return t**2 * (1 - 1 / (t + 1)) * 2
        return ((t + 2) ** 2 - 4) / 5
