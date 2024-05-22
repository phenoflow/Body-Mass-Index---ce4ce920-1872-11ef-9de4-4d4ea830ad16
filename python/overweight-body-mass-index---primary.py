# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"647L.00","system":"readv2"},{"code":"647J.00","system":"readv2"},{"code":"22A2.00","system":"readv2"},{"code":"22Z..00","system":"readv2"},{"code":"Q115.00","system":"readv2"},{"code":"Q120.00","system":"readv2"},{"code":"647F.00","system":"readv2"},{"code":"647Q.00","system":"readv2"},{"code":"647P.00","system":"readv2"},{"code":"647I.00","system":"readv2"},{"code":"647D.00","system":"readv2"},{"code":"636..12","system":"readv2"},{"code":"1621.00","system":"readv2"},{"code":"6479.00","system":"readv2"},{"code":"1623.00","system":"readv2"},{"code":"22A5.00","system":"readv2"},{"code":"647H.00","system":"readv2"},{"code":"647B.00","system":"readv2"},{"code":"647Z.00","system":"readv2"},{"code":"1625.00","system":"readv2"},{"code":"647..00","system":"readv2"},{"code":"647G.00","system":"readv2"},{"code":"Q114000","system":"readv2"},{"code":"22A..00","system":"readv2"},{"code":"Q111.00","system":"readv2"},{"code":"22A4.11","system":"readv2"},{"code":"647N.00","system":"readv2"},{"code":"647O.00","system":"readv2"},{"code":"1624.00","system":"readv2"},{"code":"6478.00","system":"readv2"},{"code":"6471.00","system":"readv2"},{"code":"22AZ.00","system":"readv2"},{"code":"647C.00","system":"readv2"},{"code":"647A.00","system":"readv2"},{"code":"22A3.00","system":"readv2"},{"code":"22A8.00","system":"readv2"},{"code":"Q115000","system":"readv2"},{"code":"647K.00","system":"readv2"},{"code":"647M.00","system":"readv2"},{"code":"22A1.00","system":"readv2"},{"code":"66C..11","system":"readv2"},{"code":"22K4.00","system":"readv2"},{"code":"1621.11","system":"readv2"},{"code":"22A4.00","system":"readv2"},{"code":"1622.00","system":"readv2"},{"code":"647E.00","system":"readv2"},{"code":"T3326BF","system":"readv2"},{"code":"Y060 BY","system":"readv2"},{"code":"T3326BB","system":"readv2"},{"code":"Y060 AY","system":"readv2"},{"code":"T3324PW","system":"readv2"},{"code":"T3326BD","system":"readv2"},{"code":"Y060 CY","system":"readv2"},{"code":"T3326BC","system":"readv2"},{"code":"T3324WC","system":"readv2"},{"code":"T3326BA","system":"readv2"},{"code":"T3326BG","system":"readv2"},{"code":"T3326BE","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('body-mass-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["overweight-body-mass-index---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["overweight-body-mass-index---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["overweight-body-mass-index---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
