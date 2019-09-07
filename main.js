$(document).ready(() => {
  const $menuButton = $('.menu-button');
  const $navDropdown = $('#nav-dropdown');

  $menuButton.on('click', () => {
    $navDropdown.show();
  })
  
  $navDropdown.on('mouseleave', () => {
    $navDropdown.hide();
  })

})

function calculateVelocity(velocity, totalTeamMembers, totalDaysOut, totalDaysInSprint, averageInjections, deploys) {
  let deployTime = deploys * 2;
  let totalHoursOutPerSprint = totalDaysOut * 6 + deployTime;
  let totalDaysOutPerSprint = totalHoursOutPerSprint / 6;
  let velocityPerPersonPerDay = velocity / (totalDaysInSprint * totalTeamMembers);
  let planFor = velocity - (totalDaysOutPerSprint * velocityPerPersonPerDay) - (averageInjections * 2);
  const x = document.getElementById("planFor").innerHTML = "Plan For " + Math.round(planFor);
}