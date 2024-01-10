from django.shortcuts import render
# your_app/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Player
from .serializers import PlayerSerializer
from django.shortcuts import get_object_or_404
import psycopg2
from psycopg2 import OperationalError

def get_current_price(player_id, connection_params):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**connection_params)
        cur = conn.cursor()

        # Execute the query for current price
        query_price = """
        SELECT current_price 
        FROM bell_curve_pricing_final 
        WHERE player_id = %s 
        ORDER BY match_date DESC 
        LIMIT 1;
        """
        cur.execute(query_price, (player_id,))
        result_price = cur.fetchone()
        cur.close()
        conn.close()

        return result_price[0] if result_price else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_total_points(player_id, connection_params):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**connection_params)
        cur = conn.cursor()

        # Execute the query for total points
        query_points = """
        SELECT total_points 
        FROM fantasy_points 
        WHERE player_id = %s 
        ORDER BY match_date DESC 
        LIMIT 1;
        """
        cur.execute(query_points, (player_id,))
        result_points = cur.fetchone()
        cur.close()
        conn.close()

        return result_points[0] if result_points else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_key_api(cricsheet_key, connection_params):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**connection_params)
        cur = conn.cursor()

        # Execute the query
        query = "SELECT key_api FROM players WHERE cricsheet_key = %s"
        cur.execute(query, (cricsheet_key,))

        # Fetch the result
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result[0] if result else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@api_view(['GET'])
def get_key_api_endpoint(request, cricsheet_key):
    try:
        # Call the function to get key_api
        connection_params = {
            'dbname': 'postgres',
            'user': 'postgres',
            'password': 'samay',
            'host': 'localhost'
        }
        key_api = get_key_api(cricsheet_key, connection_params)

        if key_api is not None:
            # Save or update the Player model (optional)
            player, created = Player.objects.get_or_create(cricsheet_key=cricsheet_key)
            player.key_api = key_api
            player.save()

            # Serialize the data (optional)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        else:
            return Response({'error': 'Player not found or an error occurred'}, status=404)

    except OperationalError as e:
        # Handle database connection errors
        return Response({'error': f'Database connection error: {e}'}, status=500)

    except Exception as e:
        # Handle other exceptions
        return Response({'error': f'An error occurred: {e}'}, status=500)

@api_view(['GET'])
def get_current_price_api(request, player_id):
    try:
        # Call the function to get current price
        connection_params = {
            'dbname': 'postgres',
            'user': 'postgres',
            'password': 'samay',
            'host': 'localhost'
        }
        current_price = get_current_price(player_id, connection_params)

        if current_price is not None:
            # Save or update the Player model
            player, created = Player.objects.get_or_create(player_id=player_id)
            player.current_price = current_price
            player.save()

            # Serialize the data
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        else:
            return Response({'error': 'Player not found or an error occurred'}, status=404)

    except OperationalError as e:
        # Handle database connection errors
        return Response({'error': f'Database connection error: {e}'}, status=500)

    except Exception as e:
        # Handle other exceptions
        return Response({'error': f'An error occurred: {e}'}, status=500)

@api_view(['GET'])
def get_total_points_api(request, player_id):
    try:
        # Call the function to get total points
        connection_params = {
            'dbname': 'postgres',
            'user': 'postgres',
            'password': 'samay',
            'host': 'localhost'
        }
        total_points = get_total_points(player_id, connection_params)

        if total_points is not None:
            # Save or update the Player model
            player, created = Player.objects.get_or_create(player_id=player_id)
            player.total_points = total_points
            player.save()

            # Serialize the data
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        else:
            return Response({'error': 'Player not found or an error occurred'}, status=404)

    except OperationalError as e:
        # Handle database connection errors
        return Response({'error': f'Database connection error: {e}'}, status=500)

    except Exception as e:
        # Handle other exceptions
        return Response({'error': f'An error occurred: {e}'}, status=500)
