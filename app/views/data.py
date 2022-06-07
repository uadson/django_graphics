from random import randint

from chartjs.views.lines import BaseLineChartView


class DataJSONView(BaseLineChartView):
    def get_labels(self):
        """
        Returns 12 labels for representation of x
        """
        labels = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]

        return labels

    def get_providers(self):
        """
        Returns the datasets names
        """
        datasets = [
            "Python",
            "Algorithms",
            "Data structure",
            "Functions",
            "OOP",
            "Framework",
        ]

        return datasets

    def get_data(self):
        """
        Returns datasets to plot the chart;
        Cach row represents a dataset;
        Each column represents a label.
        """
        data = []

        for row in range(6):
            for column in range(12):
                months = [
                    # jan
                    randint(1, 201),
                    # feb ...
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                    randint(1, 201),
                ]

            data.append(months)

        return data
