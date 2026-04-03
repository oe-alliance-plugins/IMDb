from setuptools import setup
import setup_translate

pkg = 'Extensions.IMDb'
setup(name='enigma2-plugin-extensions-imdb',
       version='3.0',
       description='query movie details from the Internet Movie Database',
       package_dir={pkg: 'IMDb'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'imdb.png', 'no_poster.png', 'starsbar_empty.png', 'starsbar_filled.png', 'maintainer.info', 'setup.xml', 'keymap.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
