#!/usr/bin/env python3
"""Verifica DOIs del corpus contra Crossref API."""
import requests
import json
import time
import sys

# DOIs extraídos de literatura_procesada.md y literatura_procesada_v2.md
# Solo los que tenían DOI verificable (no [UNVERIFIED], no SIN DOI)
dois = [
    # Bloque 1
    "10.1088/0264-9381/11/5/073",
    "10.1088/1361-6382/abdf16",
    "10.1088/1361-6382/aae326",
    "10.1088/0264-9381/21/24/011",
    "10.1155/2013/482734",
    "10.1088/0264-9381/14/11/002",
    "10.1007/JHEP08(2022)288",
    "10.1103/PhysRevD.53.7365",
    "10.1088/0264-9381/16/12/314",
    "10.1088/0264-9381/14/7/011",
    "10.1088/0264-9381/19/6/308",
    # Bloque 2
    "10.1016/j.actaastro.2018.08.035",
    "10.3847/2041-8213/aa619b",
    "10.1021/acsphotonics.9b00484",
    "10.1140/epjp/s13360-020-00542-1",
    "10.1039/D1NA00747E",
    "10.1016/j.actaastro.2018.05.018",
    "10.3847/1538-4357/aa5da6",
    "10.3847/1538-4357/aa8c73",
    # Bloque 3
    "10.1016/j.actaastro.2011.01.010",
    "10.1016/j.actaastro.2012.08.010",
    "10.1016/j.actaastro.2015.07.032",
    "10.1016/j.actaastro.2009.01.054",
    "10.1063/1.1867171",
    "10.2514/2.5661",
    "10.2514/2.5182",
    "10.1016/j.actaastro.2009.11.009",
    "10.2514/2.5969",
    "10.2514/1.A33146",
    "10.1063/1.1867222",
    "10.2514/6.2010-622",
    # Bloque 4
    "10.1017/S1473550419000259",
    "10.1017/S1473550420000257",
    "10.1007/978-981-33-6448-6_7",
    "10.55613/jeet.v25i1.41",
    "10.1017/S1473550407003709",
    "10.1017/S1473550412000419",
    "10.1016/j.actaastro.2013.04.002",
    # Bloque 5
    "10.1103/PhysRevA.82.023819",
    "10.1140/epjst/e2010-01305-5",
    "10.1016/j.scriptamat.2016.10.018",
    "10.1016/j.jeurceramsoc.2019.04.050",
    "10.1111/jace.17059",
    "10.1016/j.fusengdes.2016.03.069",
    "10.1088/2053-1583/2/2/021002",
    "10.1021/acs.nanolett.0c02572",
    # Bloque 6
    "10.1017/S1473550417000180",
    "10.1103/PhysRevA.49.678",
    "10.1002/andp.19975090505",
    "10.1109/TMTT.1984.1132833",
    # Bloque 7
    "10.1016/j.physletb.2007.09.041",
    "10.1119/1.15620",
    "10.1103/PhysRevD.39.3182",
    "10.1103/PhysRevD.98.064041",
    "10.1103/PhysRevD.96.104057",
    "10.1007/BF00696109",
    "10.1038/nphys2460",
    "10.1038/nature07121",
    # Bloque 8
    "10.2514/1.13331",
    "10.1088/2058-7058/31/2/13",
    "10.1007/978-1-4419-8017-5",
    "10.1051/0004-6361/201322293",
    "10.1089/ast.2013.1088",
    "10.1089/ast.2017.1733",
    # Bloque 9
    "10.1016/j.srt.2022.11.014",
    # Bloque 10
    "10.3847/1538-4357/aae380",
    "10.1017/S1473550417000507",
    "10.1109/ICSOS.2017.8357206",
    "10.1109/JPROC.2011.2160609",
    "10.1117/12.528434",
    "10.1103/PhysRevD.102.063005",
    "10.1038/nphys629",
    "10.3847/1538-3881/ab5dca",
    "10.1109/AERO50100.2021.9438311",
    "10.1109/FREQ.2009.5168170",
    "10.1109/FREQ.2007.4319282",
    "10.1109/ISIT.1995.531138",
    "10.1049/iet-com.2013.0081",
    # Bloque 11
    "10.1029/2021SW002751",
    "10.3847/1538-4357/aa7da6",
    "10.1016/j.asr.2021.05.021",
    "10.1016/j.actaastro.2022.04.030",
    "10.1142/S225117171840003X",
    "10.1007/s11214-020-00687-6",
    "10.1088/0004-637X/740/1/17",
    "10.1093/mnras/sty544",
    "10.1016/j.pss.2021.105291",
    "10.1089/ast.2018.1879",
    "10.1016/j.lssr.2017.07.005",
    "10.1016/j.nimb.2018.04.034",
    "10.1016/j.lssr.2019.03.004",
    "10.1016/j.pss.2019.104810",
    "10.1016/j.ijimpeng.2015.06.019",
    "10.1063/5.0046269",
    "10.2514/1.A34952",
    # Bloque 12
    "10.2514/3.26230",
    "10.1088/2399-6528/aa927e",
    "10.1016/j.actaastro.2016.07.005",
    "10.3847/2041-8213/835/2/L32",
    "10.3847/1538-3881/aa813f",
    "10.2514/1.8580",
    "10.1016/j.actaastro.2019.12.013",
    "10.2514/6.2004-3567",
    # Bloque 13
    "10.1109/ICT.1996.553506",
    "10.1016/S0149-1970(01)00005-1",
    "10.1080/00295450.2020.1730673",
    "10.1557/opl.2012.1060",
    "10.2514/6.2010-6598",
    "10.1016/j.nucengdes.2020.110569",
    "10.2514/6.2020-3537",
    "10.1063/1.1358045",
    "10.1063/1.1867192",
    "10.2514/6.2006-4062",
    # Bloque 14
    "10.1016/0094-5765(94)00183-4",
    "10.1109/ICSENS.2003.1279050",
    "10.1088/1748-0221/9/07/P07010",
    "10.1117/12.2239604",
    "10.1038/d41586-018-06957-2",
    "10.1038/ncomms13786",
    "10.1364/CLEO_AT.2015.JTh2A.79",
    "10.1117/12.2199037",
    "10.1007/s40766-023-00040-x",
    "10.1016/j.actaastro.2022.09.039",
    # Bloque 15
    "10.2514/3.25513",
    "10.1117/12.2318848",
    "10.1016/j.actaastro.2016.05.013",
    "10.1016/j.actaastro.2019.07.006",
    "10.1016/j.actaastro.2008.07.005",
    # Bloque 16
    "10.1088/2041-8205/811/2/L19",
    "10.1017/S1473550418000204",
    "10.1016/j.actaastro.2019.12.009",
    "10.1016/j.astropartphys.2021.102637",
    "10.3847/1538-4357/aa8fcc",
    "10.3847/1538-3881/ab88a1",
    "10.1016/j.actaastro.2017.10.034",
    # Bloque 17
    "10.3847/1538-4357/acbac4",
    "10.1016/j.actaastro.2020.03.021",
    "10.1007/s00521-022-07282-y",
    "10.1016/j.actaastro.2021.07.018",
    "10.1109/TAES.2019.2898730",
    # Bloque 18
    "10.1016/j.futures.2018.05.001",
    "10.1016/j.actaastro.2017.09.011",
    "10.1017/S1473550417000510",
    "10.1016/j.spacepol.2020.101374",
    "10.1016/j.actaastro.2021.06.022",
    "10.1089/ast.2018.1847",
    "10.1017/S1473550420000308",
    "10.1016/j.actaastro.2019.01.019",
    "10.1007/s11214-020-00739-x",
    "10.1016/j.spacepol.2019.101355",
    "10.1016/j.spacepol.2016.08.002",
]

total = len(dois)
ok = 0
fail = 0
errors = []

print(f"Verificando {total} DOIs contra Crossref API...")
print("=" * 60)

for i, doi in enumerate(dois):
    url = f"https://api.crossref.org/works/{doi}"
    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            data = r.json()
            title = data.get("message", {}).get("title", ["TITLE NOT FOUND"])[0]
            title_short = title[:100] if len(title) > 100 else title
            ok += 1
            print(f"  [{i+1}/{total}] OK  {doi}")
            print(f"         {title_short}")
        elif r.status_code == 404:
            fail += 1
            errors.append(("NOT_FOUND", doi))
            print(f"  [{i+1}/{total}] FAIL {doi} — 404 NOT FOUND")
        else:
            fail += 1
            errors.append((f"HTTP_{r.status_code}", doi))
            print(f"  [{i+1}/{total}] FAIL {doi} — HTTP {r.status_code}")
    except Exception as e:
        fail += 1
        errors.append(("EXCEPTION", doi, str(e)))
        print(f"  [{i+1}/{total}] FAIL {doi} — {str(e)[:80]}")

    time.sleep(0.15)  # Be nice to Crossref
    if (i + 1) % 20 == 0:
        print(f"  --- Progreso: {i+1}/{total} (OK={ok}, FAIL={fail}) ---")

print("=" * 60)
print(f"\nRESULTADO FINAL:")
print(f"  Total DOIs verificados: {total}")
print(f"  OK (DOI resuelve):     {ok} ({100*ok/total:.1f}%)")
print(f"  FAIL:                  {fail} ({100*fail/total:.1f}%)")

if errors:
    print(f"\nDOIs FALLIDOS ({len(errors)}):")
    for etype, edoi, *extra in errors:
        msg = f"  {edoi} — {etype}"
        if extra:
            msg += f" ({extra[0][:60]})"
        print(msg)

# Guardar resultados
resultado = {
    "total": total,
    "ok": ok,
    "fail": fail,
    "pct_ok": round(100*ok/total, 1),
    "errors": [{"doi": e[1], "error": e[0]} for e in errors]
}

with open("/home/juan-galaz/Escritorio/paper_interestelar/doi_verification.json", "w") as f:
    json.dump(resultado, f, indent=2, ensure_ascii=False)

print(f"\nResultados guardados en doi_verification.json")
print(f"Tasa de verificación: {resultado['pct_ok']}%")
