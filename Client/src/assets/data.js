  
// pie chart data
export const PieData = {
    chart: {
        type: "pie",
        options3d: {
        enabled: true,
        alpha: 45
        }
    },
    title: {
        text: ""
    },
    subtitle: {
        text: ""
    },
    plotOptions: {

        pie: {
        innerSize: 100,
        depth: 45
        }
    },
    series: [
        {
        name: "Pecentage (%)",
        data: [
            ["Stocks", 30],
            ["Bonds", 20],
            ["REITs", 20],
            ["ETFs", 10],
            ["Cash", 20]
        ],
        point:{
            events:{
                click: function () {
                    location.href = '/#/stocks';
                }
            }
        }
    }
    ]
};