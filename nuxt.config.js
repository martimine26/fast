
export default {
  generate: {
    fallback: "404.html"
  },
  target: 'static',
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: 'Онлайн музей',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' },
      { name: 'yandex-verification', content: 'e8732267862ad8b6'},
      { name: 'google-site-verification', content: 'YGhwDZKh3VnjZdEPvFg4JNuVwT1fYcCWdnFgbdTg6_o'}
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/logotip.ico' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#bb86fc' },
  /*
  ** Global CSS
  */
  css: [
    '@/node_modules/bootstrap/dist/css/bootstrap.min.css'
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
     ['@nuxtjs/google-fonts', {
       families: {
    Roboto:[500,600],
    Rubik: true,
    'Josefin+Sans': true,
    Lato: [100, 300],
    Raleway: {
      wght: [100, 400],
      ital: [100]
    },
   }
 }],
 ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
  ],
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  }
}
