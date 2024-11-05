
import colorama
from core.localizing import LoadLocalization, LocalizedText, ColoredLocalizedText
from core.montypes import MonType, MonTypesRegistry

if __name__ == "__main__":
    #testcases
    colorama.init()
    TESTAIM = "localizing" #the module to test
    match TESTAIM:
        case "localizing":
            LoadLocalization("zh-cn")
            a = LocalizedText("types.ice")
            print(a)
            b = ColoredLocalizedText("types.ice", "light_cyan")
            print(b, b.GetBracketed())
            LoadLocalization("en-us")
            print(a, b, b.GetBracketed())
        case "montypes":
            pass