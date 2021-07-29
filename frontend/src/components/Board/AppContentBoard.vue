<template>
  <main class="main__content--board">
    <app-header-board></app-header-board>

    <div class="lists__card">
      <app-card-list></app-card-list>
    </div>

    <app-board-menu></app-board-menu>

  </main>
  <app-card-content></app-card-content>
</template>

<script>

import AppBoardMenu from "@/components/Board/AppBoardMenu";
import AppHeaderBoard from "@/components/Board/AppHeaderBoard";
import AppCardList from "@/components/Board/AppCardList";
import AppCardContent from "@/components/Board/AppCardContent";

export default {
  name: "AppContentBoard",
  components: {AppBoardMenu, AppHeaderBoard, AppCardList, AppCardContent},
  data: () => ({}),
  methods: {}
}
</script>

<style scoped>
</style>