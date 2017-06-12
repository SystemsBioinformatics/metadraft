import time

def gene_report_template(ver, ngene, ifile, db, nmg, selg, nselg, annotG, cp):
    return """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>MetaDraft Gene Report</title>
</head>
<body>
 <h2 id="page-top">MetaDraft Gene Report</h2>
 <h3>Analysis</h3>
 <p>
 <strong>Input fasta:</strong> {}<br/>
 <strong>Metaproteome used:</strong> {}<br/>
 <strong>Report date:</strong> {}<br/>
 <strong>MetaDraft version:</strong> {}
 </p>
 <!--<h3>Notes</h3>
 <p></p>-->
 <h3>Genes ({})</h3>
 <h4>Input genes not matched</h4>
 <p>{}</p>
 <h4>Genes selected</h4>
 <table width="80%" border="0" cellspacing="1" cellpadding="1">
   <tbody>{}</tbody>
 </table>
 <h4>Genes not selected</h4>
 <table width="80%" border="0" cellspacing="1" cellpadding="1">
   <tbody>{}</tbody>
</table>
 <h3>Annotation</h3>
 {}
 <p>&nbsp;</p>
 {}
</body>
</html>""".format(ifile, db, time.strftime('%y-%m-%d'), ver, ngene, nmg, selg, nselg, annotG, cp)

def reaction_report_template(ver, nreact, ifile, db, selr, nselr, annot, cp):
    return """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>MetaDraft Reaction Report</title>
</head>
<body>
 <h2 id="page-top">MetaDraft Reaction Report</h2>
 <h3>Analysis</h3>
 <p>
 <strong>Input fasta:</strong> {}<br/>
 <strong>Metaproteome used:</strong> {}<br/>
 <strong>Report date:</strong> {}<br/>
 <strong>MetaDraft version:</strong> {}
 </p>
 <!--<h3>Notes</h3>
 <p></p>-->
 <h3>Reactions ({})</h3>
 <h4>Reactions selected</h4>
 <table width="80%" border="0" cellspacing="1" cellpadding="1">
   <tbody>{}</tbody>
 </table>
 <h4>Reactions not selected</h4>
 <table width="80%" border="0" cellspacing="1" cellpadding="1">
   <tbody>{}</tbody>
</table>
 <h3>Annotation</h3>
 {}
 <p>&nbsp;</p>
 {}
</body>
</html>""".format(ifile, db, time.strftime('%y-%m-%d'), ver, nreact, selr, nselr, annot, cp)

def metabolite_report_template(ver, nmetab, ifile, db, selm, nselm, annot, cp):
    return """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>MetaDraft Metabolite Report</title>
</head>
<body>
 <h2 id="page-top">MetaDraft Metabolite Report</h2>
 <h3>Analysis</h3>
 <p>
 <strong>Input fasta:</strong> {}<br/>
 <strong>Metaproteome used:</strong> {}<br/>
 <strong>Report date:</strong> {}<br/>
 <strong>MetaDraft version:</strong> {}
 </p>
 <!--<h3>Notes</h3>
 <p></p>-->
 <h3>Metabolites ({})</h3>
 <h4>Metabolites selected</h4>
 <table width="80%" border="0" cellspacing="1" cellpadding="1">
   <tbody>{}</tbody>
 </table>
 <h3>Annotation</h3>
 {}
 <p>&nbsp;</p>
 {}
</body>
</html>""".format(ifile, db, time.strftime('%y-%m-%d'), ver, nmetab, selm, annot, cp)
