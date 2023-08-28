from romannumerals import romanNumeralConverter 

def test_romNumConverter_1_to_I_passes():
    assert romanNumeralConverter(1) == 'I'

def test_romNumConverter_2_to_II_passes():
    assert romanNumeralConverter(2) == 'II'

def test_romNumConverter_3_to_III_passes():
    assert romanNumeralConverter(3) == 'III'

def test_romNumConverter_4_to_IV_passes():
    assert romanNumeralConverter(4) == 'IV'

def test_romNumConverter_5_to_V_passes():
    assert romanNumeralConverter(5) == 'V'

def test_romanConverter_9_to_IX_passes():
    assert romanNumeralConverter(9) == 'IX'

def test_romanConverter_10_to_X_passes():
    assert romanNumeralConverter(10) == 'X'

def test_romNumConverter_20_to_XX_passes():
    assert romanNumeralConverter(20) == 'XX'

def test_romanConverter_50_to_L_passes():
    assert romanNumeralConverter(50) == 'L'

def test_romanConverter_100_to_C_passes():
    assert romanNumeralConverter(100) == 'C'

def test_romanConverter_109_to_CIX_passes():
    assert romanNumeralConverter(109) == 'CIX'