USE [master]
GO

/****** Object:  Database [szakdolgozat]    Script Date: 10/25/2014 12:43:49 ******/
CREATE DATABASE [szakdolgozat] ON  PRIMARY 
( NAME = N'szakdolgozat', FILENAME = N'c:\Program Files\Microsoft SQL Server\MSSQL10.SQLEXPRESS\MSSQL\DATA\szakdolgozat.mdf' , SIZE = 3072KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'szakdolgozat_log', FILENAME = N'c:\Program Files\Microsoft SQL Server\MSSQL10.SQLEXPRESS\MSSQL\DATA\szakdolgozat_log.ldf' , SIZE = 1024KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO

ALTER DATABASE [szakdolgozat] SET COMPATIBILITY_LEVEL = 100
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [szakdolgozat].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [szakdolgozat] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [szakdolgozat] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [szakdolgozat] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [szakdolgozat] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [szakdolgozat] SET ARITHABORT OFF 
GO

ALTER DATABASE [szakdolgozat] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [szakdolgozat] SET AUTO_CREATE_STATISTICS ON 
GO

ALTER DATABASE [szakdolgozat] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [szakdolgozat] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [szakdolgozat] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [szakdolgozat] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [szakdolgozat] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [szakdolgozat] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [szakdolgozat] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [szakdolgozat] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [szakdolgozat] SET  DISABLE_BROKER 
GO

ALTER DATABASE [szakdolgozat] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [szakdolgozat] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [szakdolgozat] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [szakdolgozat] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [szakdolgozat] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [szakdolgozat] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [szakdolgozat] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [szakdolgozat] SET  READ_WRITE 
GO

ALTER DATABASE [szakdolgozat] SET RECOVERY SIMPLE 
GO

ALTER DATABASE [szakdolgozat] SET  MULTI_USER 
GO

ALTER DATABASE [szakdolgozat] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [szakdolgozat] SET DB_CHAINING OFF 
GO

