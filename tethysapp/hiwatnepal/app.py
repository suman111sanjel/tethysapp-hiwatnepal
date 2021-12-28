from tethys_sdk.base import TethysAppBase, url_map_maker

class Hiwatnepal(TethysAppBase):
    """
    Tethys app class for Hiwatnepal.
    """
    name = 'HIWAT Streamflow Prediction Tool - Nepal'
    index = 'hiwatnepal:home'
    icon = 'hiwatnepal/images/icon.gif'
    package = 'hiwatnepal'
    root_url = 'hiwatnepal'
    color = '#16a085'
    description = ''
    tags = 'HIWAT'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)
        url_maps = (
            UrlMap(
                name='home',
                url='hiwatnepal',
                controller='hiwatnepal.controllers.index'),
            UrlMap(
                name='chartHiwat',
                url='hiwatnepal/chartHiwat',
                controller='hiwatnepal.controllers.chartHiwat'),
            UrlMap(
                name='getGeoJson1',
                url='hiwatnepal/getGeoJson1',
                controller='hiwatnepal.controllers.getGeoJson1'),
            UrlMap(
                name='getForecastCSV',
                url='hiwatnepal/getForecastCSV',
                controller='hiwatnepal.controllers.getForecastCSV'),
            UrlMap(
                name='getHistoricCSV',
                url='hiwatnepal/getHistoricCSV',
                controller='hiwatnepal.controllers.getHistoricCSV'),
        )
        return url_maps
