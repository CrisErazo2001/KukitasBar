// ApexChartPedidos.js
import React from "react";
import ApexCharts from "react-apexcharts";

const ApexChartPedidos = ({ seriesData, labelsData }) => {
  const chartSettings = {
    colors: ["#FFCA41", "#43BC13"],
    chart: {
      height: 350,
      type: 'bar',  // Cambiamos a 'bar' para una gráfica de barras
      toolbar: { show: false },
    },
    stroke: { curve: "straight", width: [0, 1] },
    dataLabels: {
      enabled: true,
      style: { fontSize: '10px', fontWeight: 500 },
    },
    xaxis: {
      type: 'category',
      categories: labelsData,
      labels: { style: { colors: "#6B859E" } },
    },
    yaxis: { show: true },
    fill: { type: "solid", opacity: 1 },
  };

  return (
    <ApexCharts options={chartSettings} series={seriesData} type="bar" height={275} />
  );
};

export default ApexChartPedidos;
