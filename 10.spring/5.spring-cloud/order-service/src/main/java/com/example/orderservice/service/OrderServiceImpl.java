package com.example.orderservice.service;

import com.example.orderservice.dto.OrderDto;
import com.example.orderservice.jpa.OrderEntity;
import com.example.orderservice.jpa.OrderRepository;
import java.util.UUID;
import lombok.extern.slf4j.Slf4j;
import org.modelmapper.ModelMapper;
import org.modelmapper.convention.MatchingStrategies;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class OrderServiceImpl implements OrderService {

  OrderRepository orderRepository;

  @Autowired
  public OrderServiceImpl(OrderRepository orderRepository) {
    this.orderRepository = orderRepository;
  }

  @Override
  public OrderDto createOrder(OrderDto orderDetails) {
    orderDetails.setOrderId(UUID.randomUUID().toString());
    orderDetails.setTotalPrice(orderDetails.getQty() * orderDetails.getUnitPrice());

    ModelMapper mapper = new ModelMapper();
    mapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
    OrderEntity orderEntity = mapper.map(orderDetails, OrderEntity.class);

    orderRepository.save(orderEntity);

    OrderDto returnValue = mapper.map(orderEntity, OrderDto.class);

    return returnValue;
  }

  @Override
  public OrderDto getOrderByOrderId(String orderId) {
    OrderEntity orderEntity = orderRepository.findByOrderId(orderId);
    OrderDto orderDto = new ModelMapper().map(orderEntity, OrderDto.class);

    return orderDto;
  }

  @Override
  public Iterable<OrderEntity> getOrdersByUserId(String userId) {
    return orderRepository.findByUserId(userId);
  }
}
