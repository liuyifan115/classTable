<template>
	<view class="content">
		<view class="table0">
			<view class="table1">
				<view style="font-size: 20rpx;">我的课程</view>
				<view><hr></view>
				<view>
					<view v-if="lesson == ''">今日无课</view>
					<view v-else>今日{{lesson}}节</view>
				</view>
			</view>
			<view class="table1">
				<view style="font-size: 20rpx;">团队课程</view>
				<view><hr></view>
				<view>
					<view v-if="teamlesson == ''">今日无课</view>
					<view v-else>今日{{lesson}}节</view>
				</view>
				<view><hr></view>
				<view style="font-size: 15rpx;">
					<view v-if="teamID == ''">暂无团队</view>
					<view v-else>团队id：{{teamID}}</view>
				</view>
			</view>
		</view>
		<view class="table0">
			<view class="button">
				<button @click="creat">创建团队</button>
			</view>
			<view class="button">
				<button @click="join">加入团队</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				lesson:uni.getStorageSync('myTable'),
				teamlesson: uni.getStorageSync('teamTable'),
				teamID : uni.getStorageSync('teamid'),
				teamname: uni.getStorageSync('teamname')
			}
		},
		onShow() {
			let that=this
			uni.request({
					url: 'http://127.0.0.1:8000/lesson/teamtable',
					method: 'POST',
					data: {
						'teamid': uni.getStorageSync('teamid')
					},
					success: (res) => {
						uni.setStorageSync('teamTable', res.data.juti)
						}
				})
		},
		methods: {
			creat() {
				let that=this
					uni.switchTab({
						url:'../creat/creat'
					})
				},
			join() {
				let that=this
					uni.switchTab({
						url:'../join/join'
					})
				},
		}
	}
</script>

<style>
	.content{
		}
	
	.table0{
		display: flex;
		background-color: white;
	}
	
	.button{
		display: flex;
		border-radius: 30rpx;
		margin: 10rpx;
		width: 500rpx;
	}
	
	.table1{
		display: flex;
		flex-direction: column;
		background-color: whitesmoke;
		border-radius: 40rpx;
		margin: 20rpx;
		padding: 15rpx;
		width: 700rpx;
		height: 225rpx;
	}
</style>
