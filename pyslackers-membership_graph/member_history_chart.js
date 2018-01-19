import $ from 'jquery';

function buildMemberHistoryChart(slackMemberMonthlyCount){
  let output_string = "";
  let obj = slackMemberMonthlyCount;
  let objSize  = Object.keys(obj).length;
  let elemStep = Math.round(objSize / 4);
  let firstObjElem  = obj[1];
  let secondObjElem = obj[elemStep];
  let thirdObjElem  = obj[elemStep * 2];
  let fourthObjElem = obj[elemStep * 3];
  let lastObjElem   = obj[objSize];

  $('#firstCount').text(firstObjElem.member_count);
  $('#firstDate').text(firstObjElem.date);
  $('#secondCount').text(secondObjElem.member_count);
  $('#secondDate').text(secondObjElem.date);
  $('#thirdCount').text(thirdObjElem.member_count);
  $('#thirdDate').text(thirdObjElem.date);
  $('#fourthCount').text(fourthObjElem.member_count);
  $('#fourthDate').text(fourthObjElem.date);
  $('#lastCount').text(lastObjElem.member_count);
  $('#lastDate').text(lastObjElem.date);
}


export default (slackMemberMonthlyCount) => {
  let chart;
  $(window).on('orientationchange pageshow resize', () => {
    if (!chart){
      chart = buildMemberHistoryChart(slackMemberMonthlyCount);
    }
    const chartElem = $('#member_history_chart');
    const chartContainer = $('#member_history_chart_container');
    chartElem.height(chartContainer.height());
    chartElem.width(chartContainer.width());
  }).trigger('resize');
};
