import sys
import re
import logging
import codecs
import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def messurment_extract(__string):
    __pattern = "km/m|l/m|l/s|l/h|km/h|km/s|km/sp|%|°c|°d|°f|°n|°r|°re|°rø|θ|µci|µl|µn|µsv|actus|adsl|akaina|ἄκαινα|almude|alqueire|amem|fist|amu|nato|aoa|aranzada|arpent|libra|arroba|ars|ath|aud|azumbre|baht|bam|bar|barleycorn|barrel|bboe|becquerel|berkovets|bes|bgn|bif|bit|bmd|boardfoot|boe|bolt|bq|brl|b/s|bsd|btn|bu|bushel|butt|bu|byn|byte.per.day|byte.per.hour|byte.per.minute|byte.per.second|byte.per.week|bzd|cable.length|cad|cal|caliber|calories.per.hour|kan|cbl|cdf|celemín|centi|centigray|centimeter|centimeter.of.mercury|centner|century|mera|ch|chf|chi²|c/kg|clf|cm|cm²|cnh|codo|copa|cortadillo|coto|coulomb.per.kilogram|crc|ct|cubic.meter|cubic.meter.per.hour|cubic.meter.per.second|cubic.mile|cubic.millimeter|cubic.ton.of.timber|cubic.yard.of.atmosphere|standard.cubic.yard|cubit|cuc|cuerda.of.puerto.rico|culeus|hose|cun²|cun|cup|cup|cve|czech.republic.koruna|daktylos|δάκτυλος|dan|day|decaliter|decare|deci|decimeter|degree|degree.per.hour|degree.per.second|degrees.celsius|degrees.delisle|degrees.fahrenheit|degrees.newton|degrees.rankine|degrees.reaumur|degrees.rømer|deka|midfoot|didrachm|δίδραχμον|digitus|finger|diobol|διώβολον|djeser|bu|dl|dm²|dn|doite|dolya|dozen|dr|dram|egp|ell|erg|fbmm|fia|fen|fkp|fluid.ounce|foot|foot.lambert|foot.length.in.inches|foot.of.water|foot.per.minute|foot.per.second.squared|fot|ft/h|ft/m|ft/s|ft|ft²|ft³/day|ft³/min|ft³/year|ft*lbs|gal|gal/day|gallon|gallon|gal/year|garnetz|gbp|gbq|g/cm³|g/dm³|geographical.mile|ggp|g/hour|gb/s|gb/m|gib/s|gigabecquerel|gigabit.per.second|gigabyte.per.day|gigabyte.per.minute|gip|g/m³|g/min|gnf|gpm|gps|grad|grain|gram|gram-force|gram-force.meter|gram.per.cubic.decimeter|gram.per.day|gram.per.litre|gram.per.minute|gram.per.square.centimeter|grano|gray|greek.numeral|gross|gtoe|guatemalan.quetzal|guinean.franc|gy|g/year|h|half-dozen|hamma|headache|hectare|hectoliter|hekteus|hemina|pint|boiler|horsepower.hour|mechanical|imperial|hour|hour.per.gibibyte|hour.per.mebibyte|hp|hp|ht|huf|hu|ils|in²|in³/day|in³/min|in³/year|inch|inch.of.water|inch.per.minute|inch.per.second.squared|indian.rupee|inr|iqd|iraqi.dinar|isdn|kav|kboe|kbq|kcal|kelvin|keramionkg|kg/day|kgf|kgf/cm²|kgf/m²|kg/l|kg/min|kg/s|kg/year|khr|kilo|kilobecquerel|km/y|kilonewton|kilopascal|kilopound|kw|mass|kilowatt|kin|kj|km|km²|km³|km/gal|km.per.gallon|km/s|kn|knet|knot|kp|kpw|krw|kw|kw*h|kyathos|l|l/km|l²|l²mt⁻³|l⁻³m|lak|land|lb|lb/day|lb/ft³|lb/hour|lb/min|lb/s|lbsf.in|lb/year|league|league|square|legua|nautical|letek|linha|linje|liter|liter-atmosphere|l/h|liter.per.hour|l/s|liter.per.second|litres.per.100.km|litres.per.10.km|livre|li|lkr|lm/ft²|lm/in²|lmt⁻²|lrd|lsl|lux|lyd|m²|m³|m³/day|m³/min|m³/year|marco|mbq|mcal|mcg|mc/kg|medio|megabecquerel|megabit.per.second|megabyte.per.day|megabyte.per.minute|megabyte.per.week|megajoule|mj|mfbm|mbdft|mbf|mga|mg/dm³|mg/l|mg/ml|mi|mib/s|microcurie|microgray|microliter|micronewton|microsievert|mil|mile|mile.per.british.gallon|mile.per.litre|mile.per.second|mile.per.year|milion|milligray|milliliter|millimeter|millimeter.of.water|millinewton|million.btu|million.of.standard.cubic.feet.of.natural.gas|millirem|millisievert|min|mina|minim|minute|mite|mj|mkg|ml|mm|mm²|mm³|mmfbm|mmbdft|mmbf|mm/s²|mn|mnt|modius|peck|moldovan.leu|mop|mpa|mpg|mr|m/s|msv|mtoe|mu|mvr|mwk|nail|namibian.dollar|nanometer|nautical.league|nautical.rhumb|naut.mi|ncm|newton|ngn|nm|n/m²|nok|nox|nt|nzd|obolus|obol|ochava|onza|ort|osi|oz/in²|ounce|ounce.per.hour|ounce.per.second|oz|ozf|oz/ft³|oz/hour|oz/min|ozt|oz/year|pace|pc/ums|panilla|pascal|pc|pdl|perch|permille|pfund|ph|phot|physical.atmosphere|tam|pim|pint|dry|pipa|pk|pkr|plethron|pln|point|pole|polegada|ponto|poppyseed|pound|poundal|ppb|psi|pt|puncheon|purpoura|hemorrhage|infections|pyad|forearm|qar|qian|qing|qt|quad|quart|quarta|quartet|quarto.de.quartilho|quarter.of.quartilho|quaternary.number|quintal|rad|radian|radian.per.hour|radian.per.second|rai.|rd|register.ton|remen|revolution.per.hour|revolution.per.second|rin|rod|romanian.leu|roman.numeral|vinculum|rood|royal.square.perche|rt|rundlet|russian.gost.shoe.size|russian.scale.in.cm|russian.traditional.shoe.size|rwandan.franc|sai|salueng|samoan.tala|sar|saudi.riyal|sb|scc|rush.rope|scr|scrupulum|small.pebble|sdg|sea.mile.per.hour|second|shaku|shao|shekel|sheng|shkalik|short|shtoff|sicilicus|sievert|skein|skot|slope.percent|slug/ft³|square.centimeter|square.decimpeda|square.foot|square.inch|square.kilometer|square.meter|square.mil|square.mile|square.millimeter|square.ped.|ordinary|square.pouce|square.toise|square.vara.of.brazil|square.vara.of.cuba|square.verst|square.yard|sri.lankan.rupee|stadium.attic|stadium.ptolemey|standard.acceleration.of.free.fall.on.earth|stere|stilb|storage.length.in.feet|stremma|tbps|t/day|teaspoon|tera|thb|thou|t/m³|tmt|tnf|toesa|tonel|tonelada|ugx|usd|uyu|uzs|vara|vedro|verst|vuv|w|watt.hour|wa|fathom|wst|xaf|xau|xdr|xpd|xpt|yard|yd|yd²|yd³|yer|zar|zepto|zhang²|zhang|zolotnik|µgy|µ|mc|µr|acceleration|quadrantal|roman|jar|ang|angstrom|angular|sweden|anomalistic|apostilb|are|armenian|dram|arshin|asb|astronomical|unit|atm|atomic|au|australian|children|female|shoe|awg|azn|bahamian|dollar|baht|gold|trading|baker's|bangladeshi|taka|barbadian|barn|oil|equivalent|bbd|bdt|beka|belize|bermudan|bezah|egg-size|bhd|bia|pound|sterling|bwp|byte|octet|caballería|cable|modem|cayman|ccf|cdma|centigram|centiliter|centum|cubic|feet|cfa|franc|bceao|cgy|chain|charka|circumference|cl|clp|cmil|cny|decimal|number|newton|rankine|reaumur|diobol|obols|dioptre|diopter|disintegrations|djeba|djf|dkk|dm|dm³|little|double|palm|famn|fanthom|fanegada|centeno|rye|fanga|fang|zhang|fathom|fc|common|femto|fen|fever|fjd|centimeters|millimeters|cfp|ft³|ft³/h|ft³/s|ft*lbf/s|ft/s²|gallons|bit|gbps|gb/s|g/day|gel|georgian|lari|geredium|ge|gf|gf/cm²|ghs|gibibyte|gibraltar|giga|gigabit|gigabyte|gigacalories|gigatonne|gill|g/l|gmd|g/ml|gph|gprs|gregorian|g/s|gtce|gtq|guernsey|gyd|haitian|electric|hydraulic|metric|hly|average|background|radiation|megabyte|hpa|hp*h|hpm|hrk|htg|hungarian|in³|in³/h|in³/s|in/s²|iranian|rial|iteru|river|measure|jamaican|jep|jin|jod|joule|julian|kalamos|tenge|kb|kbps|kb/s|kcmil|mcm|ken|kes|kg/cm³|kg/dm³|kgf.cm|kgf.m|kg/h|kg/m³|kg/ml|kgs|khmer|khuep|kibibyte|kib/s|kilobarrel|kilobit|kilobyte|kilocalorie|kilocalories|kilojoule|squared|kilonewton|kilopond|kilotonne|kipf|klima|kmf|km/l|litre|km/s²|kn/m²|kochliarion|koku|kondylos|kosaya|sazhen|tryblion|kpa|krabiat|quarter|ksi|kvarter|kwd|kwian|cartload|kyathos|kyrgystani|som|l/100km|l⁻¹mt⁻²|l²mt⁻²|l³|labor|laotian|kip|last|lbf|lb/gal|lb/in³|lbp|lbsf.ft|lb/yd³|l/day|lebanese|por|grado|the|lesotho|loti|leuga|l/h|liang|liberian|balance|lichas|lieue|post|metrique|picosecond|lispund|litres|litron|li|lm/cm²|l/min|lm/m²|log|long|hundredweight|ton|l/s|lte|lumen|lx|l/year|m³/h|m³/s|macanese|pataca|mace|troy|mad|malagasy|ariary|malaysian|ringgit|male|manzana|rica|honduras|maquia|mark|mauritian|rupee|mbit|mbps|mb/s|mcf|mci|mdl|mebibyte|medimnos|mega|megabit|megacalorie|meganewton|megapascal|megatonne|meh|nedjes|short|meio-quartilho|half-quartilho|meter-candle|mg|mg/cm³|mgf|mg/m³|mgy|mi³|micro|microgram|microinch|micrometre|micron|microroentgen|milla|mille|passus|millibar|millicurie|milligram-force|milligrave-force|torr|million|board-feet|normal|meters|natural|gas|milliphot|milliroentgen|mina|minot|mithqal|mkd|mmbtu|mmk|mn|mn/m²|modius|castrensis|military|moio|mondopoint|monnme|moroccan|dirham|moyo|mo|mph|mro|m/s²|mtce|mur|mu|mw|mxn|myr|mzn|nad|nbiw|n/cm²|netherlands|antillean|guilder|newton|nio|nit|nm|n/mm²|wrist|tip|meddle|ounce-force|oxybathon|oz/day|oz/gal|oz/in³|oz/s|oz/yd³|pb|pc³|large|pen|percent|perche|pertica|pes|peta|petabyte|pgk|philippine|php|pica|pico|pie|pied|pixel|planck|area|energy|power|temperature|time|platinum|plm|quadrada|pollex|thumb|pood|pote|pous|ppm|pulgada|punto|px|pyg|shift|rem|rev|apostrophus|ron|rope|rsd|rub|rutherford|rwf|helena|dobra|basket|sbd|scf|shaku|shao|sheng|shesep|shp|leone|siliqua|carob|seed|singapore|si|skeppspund|sll|slope|slug/in³|slug|slug/yd³|sok|vacuum|akt|ped|legal|republic|el|salvador|guatemala|nicaragua|principe|venezuela|panama|columbia|srd|ssp|stadium|olympic|stade|stater|weight|std|sthene|stone|storage|surinamese|svc|swedish|krona|syderic|synodic|syrian|tael|talent|tamlueng|tb/s|tce|tebibyte|terabit|terabyte|ternary|th²|thai|thang|therm|t/h|thousand|mils|tib/s|tjs|t/min|tnd|toe|toise|ton-force|tonnage|tnt|triens|third|trihemitetartemorion|trinidad|tobago|triobol|tritartemorion|tetartemoria|tropic|t/s|tsun|tum|tun|turkish|lira|manat|twd|t/year|uah|uger|calorie|ukrainian|hryvnia|umts|hspa|uruguayan|usb|cable|usrt|uzbekistan|va|cuadrada|brazil|cuba|vef|vershok|vietnamese|dong|vnd|volt-ampere|watt|xag|xcd|xof|xpf|yemeni|yin|yip|pinch|yotta|yugada|zambian|kwacha|zentner|zetta|zmw|zwl|km/m|m|l|y"
    matches = re.finditer(r"\b([0-9]*)(%s)\b"%__pattern,__string,flags=re.IGNORECASE)
    __entities = []
    for m in matches:
        obj = {'messure':'','str_span':[m.start(),m.end()]}
        obj['messure'] = m.group(2).strip()
        __entities.append(obj)
    return __entities

def main():
    #string = " mph m lol 60 km/s 50km/h km/sp 156.23 adsl b/s cubic.yard.of.atmosphere ἄκαινα cun² czech.republic.koruna deka g/dm³ kn mj pk ppb square zwl fc ton ppm l/s kg/ml"
    #print(messurment_extract(string))
    named_entities = []
    input_file = codecs.open('messure_data.txt', encoding='utf-8')
    logger.info('file opened')
    for line in input_file:
        #logger.info('string converted to utf-8')
        named_entities.append({
                "sentence": line,
                "tags": messurment_extract(line)
                })
    logger.debug('%s',np.array(named_entities))
    input_file.close()
    logger.info('file closed')

    input_file = codecs.open('messure_ans.txt', encoding='utf-8')
    logger.info('testing file open')
    correct = 0
    total = 0
    for i,words in enumerate(input_file):
        word_lis = words.rstrip().split(',')
        for j,word in enumerate(word_lis):
            total += 1
            if word == named_entities[i]['tags'][j]['messure']:
                correct += 1
    input_file.close()
    logger.info('testing file closed')
    logger.debug('Accuracy: %s (%s out of %s)',str(100*correct/total),str(correct),str(total))
    return None

if __name__=="__main__":
    main()
