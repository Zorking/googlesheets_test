function doPost(e) {
  var payload = JSON.parse(e.postData.contents);
  var ss = SpreadsheetApp.openById('YOUR_GOOGLE_SH');
  var sheet = ss.getSheets()[0];
    var q = sheet.appendRow(payload);
  var qwer  = sheet.getRange(1, 1, sheet.getLastRow(), sheet.getLastColumn()).getValues();
  var i = qwer.length -1;
  while (i >= 0) { 
    if (qwer[i][0] == payload[0] && qwer[i][1] == payload[1]) {
      var output = qwer[i][2];
      break;
    }
      i--;
  } 
  return ContentService.createTextOutput(JSON.stringify(output))
    .setMimeType(ContentService.MimeType.JSON);
}
