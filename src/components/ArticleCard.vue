<template>
  <v-flex xs12 xm6 md4>
    <v-card style="border-radius: 0px" round>
      <v-card-media class="white--text" v-bind:src="article.head_img_url" height="200px">
        <v-container fill-height fluid>
          <v-layout fill-height>
            <v-flex xs12 align-end flexbox>
              <span class="headline">{{ article.title }}</span>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-media>
      <v-card-text primary-title>
        {{ article.content }}
      </v-card-text>
      <v-card-actions xs12 sm3>
        <v-spacer></v-spacer>
        <v-btn @click="favouriteArticle" icon small>
          <v-icon :color="(favored ? 'blue' : 'orange')" small>thumb_up</v-icon>
        </v-btn>
        <v-btn @click.stop="" color="orange" flat>查看</v-btn>
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  props: {
    article: {
      type: Object,
      required: true
    }
  },
  data: () => {
    return ({
      favored: false
    })
  },
  methods: {
    favouriteArticle: function () {
      this.favored = !this.favored
    }
  }
}
</script>

<style>

</style>
