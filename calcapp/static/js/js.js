
$(document).ready(function() {

$(".select").change(function() {
	var exploit_factors = (parseInt($("#q1").val()) + parseInt($("#q2").val())
	             + parseInt($("#q3").val()) + parseInt($("#q4").val())) / 4.0;

	var tech_impact = (parseInt($("#q5").val()) + parseInt($("#q6").val())) / 2.0;

	var business_impact = (parseInt($("#q7").val()) + parseInt($("#q8").val())) / 2.0;

	var score = (exploit_factors + tech_impact + business_impact) / 3.0;

	var criticality = "P1";
	if (score < 1.8)
		criticality = "P4 Trivial";
	else if (score < 3.6)
		criticality = "P3 Normal";
	else if (score < 5.4)
		criticality = "P2 Major";
	else if (score < 7.2)
		criticality = "P2 Critical";
	else
		criticality = "P1 Blocker";

	$("#criticality").html(criticality);
});

});



