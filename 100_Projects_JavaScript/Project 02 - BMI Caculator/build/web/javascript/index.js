const btnEl = document.getElementById("btn");
const bmiInputEl = document.getElementById("bmi-result");
const weightConditionEl = document.getElementById("weight-condition");

function calculateBMI() {
  const heightValue = document.getElementById("height").value / 100;
  const weightValue = document.getElementById("weight").value;

  const bmiValue = weightValue / (heightValue * heightValue);

  bmiInputEl.value = bmiValue;

  if (bmiValue < 18.5) {
    weightConditionEl.innerText = "Gầy ốm";
  } else if (bmiValue >= 18.5 && bmiValue <= 24.9) {
    weightConditionEl.innerText = "Bình thường";
  } else if (bmiValue >= 25 && bmiValue <= 29.9) {
    weightConditionEl.innerText = "Thừa cân";
  } else if (bmiValue >= 30 && bmiValue <= 34.9) {
    weightConditionEl.innerText = "Béo phì cấp độ 1";
  } else if (bmiValue >= 35 && bmiValue <= 39.9) {
    weightConditionEl.innerText = "Béo phì cấp độ 2";
  } else if (bmiValue >= 40) {
    weightConditionEl.innerText = "Béo phì cấp độ 3";
  } else if (bmiValue == 0) {
    weightConditionEl.innerText = "Vui lòng nhập các thông tin cần thiết";
  }
}

btnEl.addEventListener("click", calculateBMI);
