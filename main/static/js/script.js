var today = new Date().toISOString().split('T')[0];
var date =new Date();
document.getElementById("startDate").setAttribute('min', today);
//document.getElementById("startDate").setAttribute('value', today);
var tommorow = new Date(date.setTime(date.getTime() + 1 * 86400000 )).toISOString().split('T')[0];

document.getElementById("endDate").setAttribute('min', tommorow);

function validateStartAndEndDatesDifferences(){
    var startDateValue = document.forms["OfferInfoForm"]["minTripStartDate"].value;
    var endDateValue = document.forms["OfferInfoForm"]["endDate"].value;
    var isValid = false;

    if(startDateValue != "" && endDateValue != "") {
        var timeDiff = (new Date(endDateValue).getTime()) - (new Date(startDateValue).getTime());
        var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24)); 
   
        if(diffDays >= 1){
            document.getElementById("lengthOfStay").value = diffDays;
            isValid = true;
        }
        else
        {
            document.getElementById("lengthOfStay").value = "";
            alert("choose valid start and end date values");
        }
    }

    return isValid;
}

function validateForm() {
    var isValid = true;

    var destinaionValue = document.forms["OfferInfoForm"]["destinationName"].value;
    if (endDateValue == "") {
        alert("Destination must be filled");
        isValid = false;
    } 

    var startDateValue = document.forms["OfferInfoForm"]["minTripStartDate"].value;
    if (startDateValue == "") {
        alert("Start date must be filled");
        isValid = false;
    }

    var endDateValue = document.forms["OfferInfoForm"]["endDate"].value;
    if (endDateValue == "") {
        alert("End date must be filled");
        isValid = false;
    }

    if(isValid){
        isValid = validateStartAndEndDatesDifferences();
    }

    return isValid;
}
